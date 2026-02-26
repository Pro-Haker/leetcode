package main

func twoSum(nums []int, target int) []int {
	var num_map map[int]int
	num_map = make(map[int]int)

	for i, num := range nums {
		complement := target - num
		_, val_in_map := num_map[complement]

		if val_in_map {
			return([]int{num_map[complement], i})
		}
		num_map[num] = i
	}

	return []int{}
}
