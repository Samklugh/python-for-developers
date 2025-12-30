#the data types  in python are as follows:

song_1 = "223 seconds"  # string
song_2 = 223  # integer
song_3 = 4.5  # float
is_favorite = True  # boolean

# Displaying the data types

song_4 = 223
song_5 = 4.8

duration_sum = song_4 + song_5

print(f"the song duration is {duration_sum}")  # Output: <class 'float'>

#string concatenation
artist_1 = "Taylor"
artist_2 = "Swift"
full_artist_name = artist_1 + " " + artist_2
print(f"Full artist name: {full_artist_name}")  # Output: Full artist name: Taylor Swift

#converting string to integer
song_duration_str = "300"   
      #OR
song_duration_int = int(song_duration_str)

# converting number to string
song_duration_int = 300
song_duration_str = str(song_duration_int)  
print(f"Song duration as string: {song_duration_str}")  # Output: Song duration as string: 300