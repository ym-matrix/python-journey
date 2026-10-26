def checkout():
    # Keep track of the running cost and number of items
    total = 0
    count = 0
    moreItems = True

    # Continue collecting prices until the user enters 0
    while moreItems:
        price = float(input('Enter price of item (0 when done): '))
        if price != 0:
            count = count + 1
            total = total + price
            # Show the cost accumulated so far
            print('Subtotal: $', total)
        else:
            moreItems = False

    # Calculate and display the checkout summary
    average = total / count
    print('Total items:', count)
    print('Total $', total)
    print('Average price per item: $', average)

# Run the checkout function
checkout()