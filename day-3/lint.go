package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"strings"
)

func main() {
	input, err := ioutil.ReadFile("input.txt")
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	lines := strings.Split(string(input), "\n")
	total := 0
	currentline := 0

	for ln, line := range lines {
		half := len(line) / 2
		firstHalf := line[:half]
		secondHalf := line[half:]

		firstHalfRunes := []rune(firstHalf)
		secondHalfRunes := []rune(secondHalf)

		for i, firstHalfRune := range firstHalfRunes {
			for j, secondHalfRune := range secondHalfRunes {
				if firstHalfRune == secondHalfRune {
					if currentline != ln {
						continue
					} else { 
						currentline += 1
					}

					println("Found duplicate:", string(firstHalfRune))
					total += priority(string(firstHalfRune))
					secondHalfRunes = append(secondHalfRunes[:j], secondHalfRunes[j+1:]...)
					firstHalfRunes = append(firstHalfRunes[:i], firstHalfRunes[i+1:]...)

				}
			}
		}

	}	
	fmt.Println("Total:", total)
	
}

func priority(item string) int {
	priority := 0
	// a = 1, z = 26
	// A = 27, Z = 52
	if item >= "a" && item <= "z" {
		priority = int(item[0]) - 96
	}
	if item >= "A" && item <= "Z" {
		priority = int(item[0]) - 64 + 26
	}
	return priority
}