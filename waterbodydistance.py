import geopandas as gpd
import pandas as pd
import os
from shapely.ops import nearest_points

# Set paths (use raw strings to avoid path issues)
polygon_folder = r"C:\Users\SumeerKoirala\Downloads\deliverables final\deliverables final\250_meters"
point_shapefile = r"D:\500 meters\centrod_plot.shp"
output_excel = r"C:\Users\SumeerKoirala\Downloads\deliverables final\deliverables final\water_body_distances_250_buffer.xlsx"

# Load the point shapefile
points_gdf = gpd.read_file(point_shapefile)

# Print CRS of the points file
print(f"Points CRS: {points_gdf.crs}")

# Ensure the CRS (coordinate system) is set
if points_gdf.crs is None:
    points_gdf = points_gdf.set_crs("EPSG:4326")  # Adjust CRS as needed
    print(f"Assigned CRS to points: {points_gdf.crs}")

# Data collection
data = []

# Iterate over all polygon shapefiles in the folder
for file in os.listdir(polygon_folder):
    if file.endswith(".shp"):  # Ensure only shapefiles are processed
        polygon_path = os.path.join(polygon_folder, file)
        polygons_gdf = gpd.read_file(polygon_path)

        # Print CRS of polygons
        print(f"Processing {file} - Polygons CRS: {polygons_gdf.crs}")

        # Assign CRS if missing
        if polygons_gdf.crs is None:
            polygons_gdf = polygons_gdf.set_crs(points_gdf.crs)
            print(f"Assigned CRS to {file}: {polygons_gdf.crs}")

        # Ensure CRS matches before transformation
        if polygons_gdf.crs != points_gdf.crs:
            print(f"Converting CRS for {file} to match points CRS.")
            polygons_gdf = polygons_gdf.to_crs(points_gdf.crs)

        # Check unique values in class_0
        print(f"Unique class_0 values: {polygons_gdf['class_0'].unique()}")

        # Filter polygons where class_0 == 9 (water bodies)
        if "class_0" in polygons_gdf.columns:
            water_bodies = polygons_gdf[polygons_gdf["class_0"] == 9]
        else:
            print(f"Skipping {file} - 'class_0' column missing.")
            continue

        if not water_bodies.empty:
            # Process all water bodies (multiple polygons can be present)
            for _, polygon in water_bodies.iterrows():
                # Use polygon boundary instead of centroid
                boundary = polygon.geometry.boundary  # Get the boundary of the polygon
                nearest_point = nearest_points(boundary, points_gdf.unary_union)[1]  # Nearest point on the boundary
                distance = boundary.distance(nearest_point)  # Compute distance from boundary to nearest point

                # Extract relevant attributes
                class_0 = 9
                final = water_bodies["Final"].iloc[0] if "Final" in water_bodies.columns and not water_bodies.empty else "N/A"

                # Store results for each water body
                data.append([file, class_0, final, distance])

# Convert results to DataFrame
df = pd.DataFrame(data, columns=["id", "Class_0", "Final", "Shortest_Distance_to_Boundary"])

# Save to Excel
df.to_excel(output_excel, index=False)

print(f"Excel file saved: {output_excel}")