import gpxpy
import folium

def plotGpxOnMap(fileList, output="index.html"):
    m = folium.Map(location=[42.342855, 13.40408],zoom_start=14)

    genPoints=[]

    for fl in fileList:
        
        with open(fl, "r") as f:
            gpx = gpxpy.parse(f)

        
        points = []
        
        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    points.append((point.latitude, point.longitude))

        genPoints+=points


        
        

        
        folium.PolyLine(points, color="blue", weight=4).add_to(m)

        folium.CircleMarker(
            location=points[0],
            radius=2,          
            color="red",       
            fill=True,
            fill_opacity=0.7,
            fill_color="red"   
        ).add_to(m)


        #folium.Marker(points[0], popup="Start").add_to(m)
        #folium.Marker(points[-1], popup="End").add_to(m)
    
    folium.CircleMarker(
            location=genPoints[-1],
            radius=2,          
            color="red",       
            fill=True,
            fill_opacity=0.7,
            fill_color="red"   
        ).add_to(m)
    #print(genPoints[0])

    #m.location=genPoints[0]

    m.save(output)
       


if __name__ == "__main__":
    files = ["D:\\dionigi\\\Downloads\\1-tappa-tratturo-magno.gpx","D:\\\dionigi\\\Downloads\\2-tappa-tratturo-magno.gpx","D:\\\dionigi\\\Downloads\\3-tappa-tratturo-magno.gpx","D:\\\dionigi\\\Downloads\\4-tappa-tratturo-magno.gpx","D:\\\dionigi\\\Downloads\\5-tappa-tratturo-magno.gpx","D:\\\dionigi\\\Downloads\\6-tappa-tratturo-magno.gpx","D:\\\dionigi\\\Downloads\\7-tappa-tratturo-magno.gpx","D:\\\dionigi\\\Downloads\\8-tappa-tratturo-magno.gpx","D:\\\dionigi\\\Downloads\\9-tappa-tratturo-magno.gpx","D:\\\dionigi\\\Downloads\\10-tappa-tratturo-magno.gpx"]
    plotGpxOnMap(files)
