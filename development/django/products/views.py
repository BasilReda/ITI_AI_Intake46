from django.shortcuts import render
from django.http import Http404

PRODUCTS = [
    {
        'id': 1,
        'name': 'Apple MacBook Air 2020 13" Intel Core i5 1.1GHz 8GB RAM 256GB SSD Space Gray | macOS',
        'price': 279.00,
        'stock_count': 12,
        'image': '/media/products/large-2020_Apple_MacBook_Air_Gray_2__09076__51390.jpg',
    },
    {
        'id': 2,
        'name': 'Apple MacBook Air 2020 13" Intel Core i7 1.2GHz 16GB RAM 512GB SSD Space Gray | macOS Sequoia',
        'price': 391.00,
        'stock_count': 5,
        'image': '/media/products/large-2020_Apple_MacBook_Air_Gray_4__17878.jpg',
    },
    {
        'id': 3,
        'name': 'Gaming PC Desktop AMD Ryzen 5 5500 up to 4.2GHz, Radeon RX 590 8G, 16GB DDR4, 512GB SSD, WiFi 6, RGB Fan x5, Windows 11 Home',
        'price': 32402.00,
        'stock_count': 7,
        'image': '/media/products/firstpc.webp',
    },
    {
        'id': 4,
        'name': 'Skytech Gaming Azure 3 PC, AMD Ryzen 7 9700X 3.8GHz, NVIDIA RTX 5060, 1TB NVMe SSD, 32GB DDR5 RAM 6000, 850W Gold ATX PSU, 360 ARGB AIO, Wi-Fi, Win 11',
        'price': 68792.50,
        'stock_count': 4,
        'image': '/media/products/secondpc.webp',
    },
    {
        'id': 5,
        'name': 'White Gaming Chair, Ergonomic Massage Computer Office Chair with Footrest, Adjustable Lumbar Support, Reclining Racing Chair',
        'price': 6778.60,
        'stock_count': 15,
        'image': '/media/products/first-chair.webp',
    },
    {
        'id': 6,
        'name': 'Dowinx Gaming Chair Fabric with Pocket Spring Cushion, Ergonomic Computer Chair with Footrest, 2 Sizes Available — Top Reviewed for Comfort',
        'price': 7477.00,
        'stock_count': 20,
        'image': '/media/products/second_chair.webp',
    },
]


def index(request):
    return render(request, 'products/index.html', {'products': PRODUCTS})


def show(request, pk):
    product = next((p for p in PRODUCTS if p['id'] == pk), None)
    if product is None:
        raise Http404("Product not found")
    return render(request, 'products/show.html', {'product': product})

