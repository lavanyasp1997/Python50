def dijkstra(gr, src, vert, dst):
    dis_rec = {}

    cur = src
    cur_dis = 0
    while 1:
        neb = gr.get(cur, {})
        for k, v in neb.items():
            dLis = dis_rec.get(k, [])
            dLis.append(cur_dis + v)
            dis_rec[k] = dLis
        # print(cur, neb, dis_rec)
        min_dis = 1000000000
        min_node = ""
        for node, dLis in dis_rec.items():
            if len(dLis) == vert[node] and max(dLis) < min_dis:
                min_dis = max(dLis)
                min_node = node

        if min_node in dst:
            return [min_node, min_dis]

        if min_node != '':
            cur = min_node
            cur_dis = min_dis
            del dis_rec[cur]


if __name__ == "__main__":
    # Inputs: A
    # Outputs: B C
    # INV A D 20 E 10 F 5
    # NAND2 D E B 6
    # NAND2 E F C 10
    ckt_source = "A"
    ckt_dest = ["I", "M", "K"]
    lines = ["INV A B 5 C 6 D 7 G 1 E 1 F 1",
             "NAND3 D E F J 8",
             "NAND2 B H I 9",
             "INV G H 1",
             "NAND2 C J L 4",
             "INV L M 2",
             "INV J K 3"]

    vert = {}
    g = {}
    for line in lines:
        wds = line.split(' ')
        if wds[0] == "INV":
            i = 1
            while i < len(wds):
                source = wds[i]
                adj_lis = g.get(source, {})

                j = i + 1
                while (j + 1) < len(wds) and wds[j + 1].isnumeric():
                    dest = wds[j]
                    dis = int(wds[j + 1])
                    adj_lis[dest] = dis
                    vert[dest] = 1
                    j += 2

                g[source] = adj_lis
                if (j + 1) < len(wds):
                    i = j
                else:
                    break
        elif wds[0] == "NAND2":
            i = 1
            while (i + 3) < len(wds):
                ip1 = wds[i]
                ip2 = wds[i + 1]
                op = wds[i + 2]
                dis = int(wds[i + 3])
                vert[op] = 2

                al1 = g.get(ip1, {})
                al2 = g.get(ip2, {})

                al1[op] = dis
                g[ip1] = al1
                al2[op] = dis
                g[ip2] = al2

                i += 4

        elif wds[0] == "NAND3":
            i = 1
            while (i + 4) < len(wds):
                ip1 = wds[i]
                ip2 = wds[i + 1]
                ip3 = wds[i + 2]
                op = wds[i + 3]
                dis = int(wds[i + 4])
                vert[op] = 3

                al1 = g.get(ip1, {})
                al2 = g.get(ip2, {})
                al3 = g.get(ip3, {})

                al1[op] = dis
                g[ip1] = al1
                al2[op] = dis
                g[ip2] = al2
                al3[op] = dis
                g[ip3] = al2

                i += 5

    # print(g, vert)
    print(dijkstra(g, ckt_source, vert, ckt_dest))