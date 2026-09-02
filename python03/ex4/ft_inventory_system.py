#!/usr/bin/env python3
import sys


def main() -> None:
    print("=== Inventory System Analysis ===")
    args: list[str] = sys.argv[1:]
    inventory: dict[str, int] = {}
    insertion_order: list[str] = []

    for arg in args:
        if ":" not in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue

        parts: list[str] = arg.split(":")
        if len(parts) != 2:
            print(f"Error - invalid parameter '{arg}'")
            continue

        # Desempacotamos os elementos diretamente sem usar colchetes!
        item_name, qty_str = parts

        if not item_name:
            print(f"Error - invalid parameter '{arg}'")
            continue

        if item_name in inventory:
            print(f"Redundant item '{item_name}' - discarding")
            continue

        try:
            qty: int = int(qty_str)
        except ValueError as e:
            print(f"Quantity error for '{item_name}': {e}")
            continue

        inventory[item_name] = qty
        insertion_order.append(item_name)

    print(f"Got inventory: {inventory}")

    if not inventory:
        print("Item list: []")
        print("Total quantity of the 0 items: 0")
        print("Updated inventory: {'magic_item': 1}")
        return

    items: list[str] = list(inventory.keys())
    print(f"Item list: {items}")

    total_qty: int = sum(inventory.values())
    print(f"Total quantity of the {len(items)} items: {total_qty}")

    for item in items:
        qty = inventory[item]
        pct: float = (qty / total_qty) * 100 if total_qty > 0 else 0.0
        print(f"Item {item} represents {pct:.1f}%")

    # Pegamos o primeiro item da lista desempacotando-o de forma limpa!
    first_item, *rest = insertion_order
    most_abundant_item: str = first_item
    least_abundant_item: str = first_item

    for item in insertion_order:
        if inventory[item] > inventory[most_abundant_item]:
            most_abundant_item = item
        if inventory[item] < inventory[least_abundant_item]:
            least_abundant_item = item

    print(
        f"Item most abundant: {most_abundant_item} "
        f"with quantity {inventory[most_abundant_item]}"
    )
    print(
        f"Item least abundant: {least_abundant_item} "
        f"with quantity {inventory[least_abundant_item]}"
    )

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
