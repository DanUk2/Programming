# For the following, given the first line write the line(s) of
# code that will give you the output in bold. For each one there may
# be more than one correct answer; just give one.

a_list = [3, 5, 6, 12]
b_list = []
c_list = []
d_list = []
e_list = []

for n in a_list:
    if n < 4:
        b_list.append(n)
print (b_list)

for n in a_list:
    if n > 3:
        c_list.append(n)
print (c_list)

print(sorted(a_list, reverse=True))

for n in a_list:
    d_list.append(n*3)
print(d_list)


for n in a_list:
    if n%2 == 0:
        e_list.append('True')
    else:
        e_list.append('False')
print(e_list)

##

months = ["jan", "feb", "march", "april", "may", "june", "july", "aug", "sept", "oct", "nov", "dec"]
while True:
    date = input("dd/mm/yyyy: ")

    if "/" in date:
        number_of_slashes = date.count("/")
        if number_of_slashes == 2:
            string_day, string_month, string_year = date.split("/")

            if len(string_year) == 4:
                if (int(string) <= 31 and int(string_day) > 0) and (int(string_month) > 0 and int (string_month) < 13):

                    mon = months[int(string_month)-1]
                    print("the date is %s %s, %s " % (mon, string_day, string_year))
