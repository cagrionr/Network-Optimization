import math


def TotalDelay(path_nodes):
    """
    Yoldaki toplam gecikmeyi hesaplar

    Args:
        path_nodes: Node objelerinin listesi [node1, node2, node3, ...]

    Returns:
        float: Toplam gecikme (ms)
    """
    if len(path_nodes) < 2:
        return 0

    total_delay = 0

    # Link gecikmeleri + ara düğüm işlem gecikmelerini topla
    for i in range(len(path_nodes) - 1):
        current_node = path_nodes[i]
        next_node = path_nodes[i + 1]

        # Ara düğümlerin işlem gecikmesini ekle (S ve D hariç)
        if i > 0:  # İlk düğüm (kaynak) değilse
            total_delay += current_node.ProcessingDelay

        # Link gecikmesini bul
        link = current_node.getLinkTo(next_node.NodeId)
        if link:
            total_delay += link.LinkDelay
        else:
            return float('inf')  # Link yoksa sonsuz gecikme

    return total_delay


def TotalReliability(path_nodes):
    """
    Yoldaki toplam güvenilirliği hesaplar

    Args:
        path_nodes: Node objelerinin listesi

    Returns:
        float: Toplam güvenilirlik (0-1 arası)
    """
    if len(path_nodes) < 2:
        return 0

    total_reliability = 1.0

    # Tüm node güvenilirliklerini çarp
    for node in path_nodes:
        total_reliability *= node.NodeReliability

    # Tüm link güvenilirliklerini çarp
    for i in range(len(path_nodes) - 1):
        current_node = path_nodes[i]
        next_node = path_nodes[i + 1]

        link = current_node.getLinkTo(next_node.NodeId)
        if link:
            total_reliability *= link.LinkReliability
        else:
            return 0  # Link yoksa güvenilirlik 0

    return total_reliability


def ReliabilityCost(path_nodes):
    """
    Güvenilirlik maliyetini hesaplar (minimize edilecek)

    Args:
        path_nodes: Node objelerinin listesi

    Returns:
        float: Güvenilirlik maliyeti
    """
    if len(path_nodes) < 2:
        return float('inf')

    reliability_cost = 0

    # Tüm node güvenilirliklerinin negatif log'unu topla
    for node in path_nodes:
        if node.NodeReliability > 0:
            reliability_cost += -math.log(node.NodeReliability)
        else:
            return float('inf')

    # Tüm link güvenilirliklerinin negatif log'unu topla
    for i in range(len(path_nodes) - 1):
        current_node = path_nodes[i]
        next_node = path_nodes[i + 1]

        link = current_node.getLinkTo(next_node.NodeId)
        if link and link.LinkReliability > 0:
            reliability_cost += -math.log(link.LinkReliability)
        else:
            return float('inf')

    return reliability_cost


def ResourceCost(path_nodes):
    """
    Kaynak kullanım maliyetini hesaplar

    Args:
        path_nodes: Node objelerinin listesi

    Returns:
        float: Kaynak maliyeti
    """
    if len(path_nodes) < 2:
        return float('inf')

    resource_cost = 0

    # Her link için ters bant genişliği maliyetini topla
    for i in range(len(path_nodes) - 1):
        current_node = path_nodes[i]
        next_node = path_nodes[i + 1]

        link = current_node.getLinkTo(next_node.NodeId)
        if link and link.Bandwidth > 0:
            resource_cost += 1000.0 / link.Bandwidth  # 1 Gbps = 1000 Mbps
        else:
            return float('inf')

    return resource_cost


def TotalCost(path_nodes, w_delay=0.33, w_reliability=0.33, w_resource=0.34):
    """
    Ağırlıklı toplam maliyet fonksiyonu

    Args:
        path_nodes: Node objelerinin listesi
        w_delay: Gecikme ağırlığı
        w_reliability: Güvenilirlik ağırlığı
        w_resource: Kaynak ağırlığı

    Returns:
        float: Toplam maliyet
    """
    # Normalize etmek için maksimum değerleri varsayalım
    MAX_DELAY = 15 * len(path_nodes)  # Her link max 15ms
    MAX_RELIABILITY_COST = -math.log(0.95) * len(path_nodes) * 2  # Her node+link min 0.95
    MAX_RESOURCE_COST = (1000.0 / 100) * len(path_nodes)  # Min BW 100 Mbps

    delay = TotalDelay(path_nodes)
    rel_cost = ReliabilityCost(path_nodes)
    res_cost = ResourceCost(path_nodes)

    # Normalize et
    norm_delay = delay / MAX_DELAY if MAX_DELAY > 0 else 0
    norm_rel = rel_cost / MAX_RELIABILITY_COST if MAX_RELIABILITY_COST > 0 else 0
    norm_res = res_cost / MAX_RESOURCE_COST if MAX_RESOURCE_COST > 0 else 0

    return w_delay * norm_delay + w_reliability * norm_rel + w_resource * norm_res


# Test fonksiyonu
def test_metrics():
    from NodeClass import Node

    # Örnek yol oluştur
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    node1.addLinkWithParams(2, 500, 10, 0.98)
    node2.addLinkWithParams(3, 800, 5, 0.99)

    path = [node1, node2, node3]

    print(f"Total Delay: {TotalDelay(path):.2f} ms")
    print(f"Total Reliability: {TotalReliability(path):.4f}")
    print(f"Reliability Cost: {ReliabilityCost(path):.4f}")
    print(f"Resource Cost: {ResourceCost(path):.4f}")
    print(f"Total Cost: {TotalCost(path):.4f}")


if __name__ == "__main__":
    test_metrics()