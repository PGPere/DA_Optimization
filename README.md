# Dijkstra Optimization

### Application Overview

This script is a small Streamlit application that builds a predetermined network of towns connected by weighted roads, then lets the user interactively select an origin and destination. Behind the scenes it uses NetworkX’s Dijkstra algorithm to find the shortest route and its total distance. The app displays the resulting path as text and renders a network diagram with the chosen shortest‐path highlighted in red. A safety check prevents selecting the same town for both origin and destination, showing a warning instead.

[▶️ Launch the live demo](https://fz6prwwyqwqeiaiypqupe8.streamlit.app/)

