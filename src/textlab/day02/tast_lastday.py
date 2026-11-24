def sort(products):
    return sorted(products,key=lambda product: product[1])




def main():
    products = [
        ("apple", 10),
        ("banana", 5),
        ("orange", 20),
        ("grape", 5)
    ]
    result = sort(products)
    print(result)


if __name__ == "__main__":
    main()