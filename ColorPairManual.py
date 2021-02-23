import ColorPairOperations

#Print the Header
print ("{:<20} {:<20} {:<20}".format('Pair Number','Major Color', 'Minor Color'))

#Print the contents for Color code manual
for majorcolor in ColorPairOperations.MAJOR_COLORS:
  for minorcolor in ColorPairOperations.MINOR_COLORS:
    pairnumber = ColorPairOperations.get_pair_number_from_color(majorcolor,minorcolor)
    print ("{:<20} {:<20} {:<20}".format(pairnumber, majorcolor, minorcolor))
  
  

