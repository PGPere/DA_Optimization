import streamlit as st
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

def build_graph():
    edges = [
        ('Origin', 'A', 40), ('Origin', 'B', 60), ('Origin', 'C', 50),
        ('A', 'B', 10), ('A', 'D', 70),
        ('B', 'C', 20), ('B', 'D', 55), ('B', 'E', 40),
        ('C', 'E', 50),
        ('D', 'E', 10),
        ('E', 'Destination', 60),
        ('D', 'Destination', 60)
    ]
    G = nx.Graph()
    G.add_weighted_edges_from(edges)
    return G

def shortest_path(G, source='Origin', target='Destination'):
    path = nx.dijkstra_path(G, source=source, target=target, weight='weight')
    distance = nx.dijkstra_path_length(G, source=source, target=target, weight='weight')
    return path, distance

def draw_graph(G, path):
    pos = nx.spring_layout(G, seed=42)
    edge_labels = nx.get_edge_attributes(G, 'weight')

    plt.figure(figsize=(10, 6))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    path_edges = list(zip(path[:-1], path[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=3)
    st.pyplot(plt)

def main():
    st.title("Shortest Path Finder Between Towns")

    G = build_graph()
    path, distance = shortest_path(G)

    st.markdown("### Shortest Path")
    st.write(" → ".join(path))
    st.write(f"Total Distance: {distance} miles")

    st.markdown("### Network Graph")
    draw_graph(G, path)

if __name__ == '__main__':
    main()
