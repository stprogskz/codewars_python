def find_needle(haystack):
    index = haystack.index('needle')
    return f'found the needle at position {index}'


items = ['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk']
print(find_needle(items))
