# Best Fit memory allocation method for fixed partition

# Input memory blocks with size and processes with size
memory_blocks = [100, 500, 200, 300, 600]
processes = [212, 417, 112, 426]

# Initialize all memory blocks as free
allocated_blocks = [-1] * len(processes)

# Start by picking each process and check if it can be assigned to current block
for i in range(len(processes)):
    # Initialize the index of the block with the smallest free space
    min_free_index = -1
    # Loop through all memory blocks
    for j in range(len(memory_blocks)):
        # Check if the current memory block is free and its size is greater than or equal to the size of the current process
        if memory_blocks[j] >= processes[i] and allocated_blocks[i] == -1:
            # If the current block has less free space than the previous minimum, update the minimum
            if min_free_index == -1 or memory_blocks[j] < memory_blocks[min_free_index]:
                min_free_index = j
    # If a block with enough free space was found, allocate the block to the process
    if min_free_index != -1:
        allocated_blocks[i] = min_free_index
        memory_blocks[min_free_index] -= processes[i]

# Print the allocation details
print("Best Fit Allocation:")
print("Process No.\tProcess Size\tBlock No.")
for i in range(len(processes)):
    print(i+1, "\t\t", processes[i], "\t\t", allocated_blocks[i]+1 if allocated_blocks[i]!=-1 else "Not Allocated")
