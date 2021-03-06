import re

pattern = re.compile(r'(@[#]+)(?P<code>[A-Z][A-Za-z0-9]{4,}[A-Z])(@[#]+)')
count_of_code = int(input())

for _ in range(count_of_code):
    default_group = '00'
    barcode_string = input()
    b = pattern.search(barcode_string)
    if b:
        temp = b.group('code')
        digits = "".join([i for i in temp if i.isdigit()])
        if digits:
            default_group = digits
        print(f"Product group: {default_group}")
    else:
        print("Invalid barcode")

"""
Each line must not contain anything else but a valid barcode. A barcode is valid when:
    • Is surrounded with a "@" followed by one or more "#" 
    • Is at least 6  characters long (without the surrounding "@" or "#")
    • Starts with a capital letter
    • Contains only letters (lower and upper case) and digits
    • Ends with a capital letter
Examples of valid barcodes: @#FreshFisH@#, @###Brea0D@###, @##Che46sE@##, @##Che46sE@###
Examples of invalid barcodes: ##InvaliDiteM##, @InvalidIteM@, @#Invalid_IteM@#
Next you have to determine the product group of the item from the barcode. The product group is obtained by concatenating all the digits found in the barcode. If there are no digits present in the barcode, the default product group is "00".
Examples:  
@#FreshFisH@# -> product group: 00
@###Brea0D@### -> product group: 0
@##Che4s6E@## -> product group: 46
"""

# Input:
"""
6
@###Val1d1teM@###
@#ValidIteM@#
##InvaliDiteM##
@InvalidIteM@
@#Invalid_IteM@#
@#ValiditeM@#
"""
