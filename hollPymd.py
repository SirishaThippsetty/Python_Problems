n = int(input())

for row in range(1, n + 1):
    left_spaces_count = n - row
    left_spaces = " " * left_spaces_count
    row_output = left_spaces + "* " * row
    
    if(row == 1 or row == n):
        print(row_output)
    else:
        hollow_spaces_count = row - 2
        hollow_spaces = "  " * hollow_spaces_count
        row_output = left_spaces + "* " + hollow_spaces + "* "
        print(row_output)

'''
ip:4

   * 
  * * 
 *   * 
* * * * 

'''