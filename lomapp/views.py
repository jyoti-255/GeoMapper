from django.shortcuts import render
from folium import Map, Marker, Figure

def home(request):
    if request.method == "POST":
        lat = float(request.POST.get("lat"))
        lon = float(request.POST.get("lon"))
        loc = [lat, lon]  # Corrected 'on' to 'lon'
        f = Figure(width=600, height=600)
        lom = Map(location=loc, zoom_start=20).add_to(f)
        Marker(loc, tooltip="location").add_to(lom)
        lom_html = lom._repr_html_()
        return render(request, "home.html", {"msg": lom_html})
    else:
        return render(request, "home.html") 