package main

import (
	"bufio"
	"fmt"
	"os"
	"path/filepath"
	"sort"
	"strconv"
)

func main() {

	f, _ := os.Open(filepath.Base("input.txt"))

	fileScanner := bufio.NewScanner(f)

	calories := []int{}
	var currentSum int

	for fileScanner.Scan() {

		line := fileScanner.Text()

		if len(line) == 0 {
			calories = append(calories, currentSum)
			currentSum = 0
			continue
		}

		lineCalories, _ := strconv.Atoi(line)

		currentSum += lineCalories
	}

	calories = append(calories, currentSum)

	sort.Ints(calories)

	fmt.Println(calories[len(calories)-1])

}
