from collections import deque

def afficher_table_bellman(dist, pred):
    print("\n📋 Table Bellman-Ford (chemin en cours) :")
    print(f"{'Sommet':<10}{'Distance':<15}{'Prédécesseur'}")
    for i in range(len(dist)):
        d = '∞' if dist[i] == float('inf') else dist[i]
        p = pred[i] if pred[i] != -1 else "-"
        print(f"{i:<10}{str(d):<15}{p}")
    print()

def bellman_ford(capacite, cout, flot, source):
    n = len(capacite)
    dist = [float('inf')] * n
    pred = [-1] * n
    in_queue = [False] * n
    dist[source] = 0
    queue = deque([source])
    in_queue[source] = True

    while queue:
        u = queue.popleft()
        in_queue[u] = False
        for v in range(n):
            # Arc direct
            if capacite[u][v] - flot[u][v] > 0 and dist[v] > dist[u] + cout[u][v]:
                dist[v] = dist[u] + cout[u][v]
                pred[v] = u
                if not in_queue[v]:
                    queue.append(v)
                    in_queue[v] = True
            # Arc de retour
            if flot[v][u] > 0 and dist[v] > dist[u] - cout[v][u]:
                dist[v] = dist[u] - cout[v][u]
                pred[v] = -u
                if not in_queue[v]:
                    queue.append(v)
                    in_queue[v] = True

    afficher_table_bellman(dist, pred)
    return dist, pred

def flot_a_cout_minimal(capacite, cout, flot_demande):
    n = len(capacite)
    source = 0
    puits = n - 1

    flot = [[0]*n for _ in range(n)]
    cout_total = 0
    flot_envoye = 0

    while flot_envoye < flot_demande:
        dist, pred = bellman_ford(capacite, cout, flot, source)
        if dist[puits] == float('inf'):
            break  # Aucun chemin restant

        delta = flot_demande - flot_envoye
        v = puits
        while v != source:
            u = abs(pred[v])
            if pred[v] >= 0:
                delta = min(delta, capacite[u][v] - flot[u][v])
            else:
                delta = min(delta, flot[v][u])
            v = u

        v = puits
        while v != source:
            u = abs(pred[v])
            if pred[v] >= 0:
                flot[u][v] += delta
                cout_total += delta * cout[u][v]
            else:
                flot[v][u] -= delta
                cout_total -= delta * cout[v][u]
            v = u

        flot_envoye += delta

    if flot_envoye < flot_demande:
        return None, flot_envoye, cout_total
    else:
        return flot, flot_envoye, cout_total
