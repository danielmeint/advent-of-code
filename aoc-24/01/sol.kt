import java.io.File

fun main() {
    // Read input and split into left and right lists
    val (left, right) = File("input.txt").readLines()
        .map { it.split(" ").map(String::toInt) }
        .unzip()

    // Part 1: Calculate total distance
    val totalDistance = left.sorted().zip(right.sorted())
        .sumOf { (a, b) -> kotlin.math.abs(a - b) }
    println("Part 1: Total Distance = $totalDistance")

    // Part 2: Calculate similarity score
    val rightCounts = right.groupingBy { it }.eachCount()
    val similarityScore = left.sumOf { it * (rightCounts[it] ?: 0) }
    println("Part 2: Similarity Score = $similarityScore")
}
