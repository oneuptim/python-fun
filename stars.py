# x = [4, 6, 1, 3, 5, 7, 25]
# def draw_Stars(arr):
#     for i in range(len(arr)):
#         print arr[i] * "*"
#
# draw_Stars(x)

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

def draw_Stars(arr):
    for i in range(len(arr)):

        if type(arr[i]) is int:
            print arr[i] * "*"
        else:
            # output = ""
            first_letter = i[0].lower()
            # output += first_letter
            print first_letter

draw_Stars(x)
