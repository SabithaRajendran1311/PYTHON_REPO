def generate_fibonacci(n):
    sequence=[0,1]
    while len(sequence)<n:
        next_num=sequence[-1]+sequence[-2]
        sequence.append(next_num)
    return sequence
num_terms=int(input("Enter the number of terms:"))
fibonacci_seq=generate_fibonacci(num_terms)
print("fibonacci sequence:",fibonacci_seq)
    
