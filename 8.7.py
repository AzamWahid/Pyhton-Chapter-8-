def make_album(artist_name,album_name,tracks=0):
    if tracks:
        return {'name':artist_name,'title':album_name,'tracks':tracks}
    else:
        return {'name':album_name,'title':album_name}


print(make_album('azhi','ZNMD'))

print(make_album('AQ','Mai Abdul Qadir hoon'))
print(make_album('Arjeet','Sanam ry',50))