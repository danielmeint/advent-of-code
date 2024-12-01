import Data.List (sort)
import qualified Data.Map as Map

main = do
    content <- readFile "input.txt"
    let (left, right) = unzip $ map ((\[a, b] -> (a, b)) . map read . words) (lines content)

    -- Part 1
    let totalDistance = sum $ zipWith (\a b -> abs (a - b)) (sort left) (sort right)
    putStrLn $ "Part 1: Total Distance = " ++ show totalDistance

    -- Part 2
    let rightCounts = Map.fromListWith (+) [(x, 1) | x <- right]
    let similarityScore = sum [x * Map.findWithDefault 0 x rightCounts | x <- left]
    putStrLn $ "Part 2: Similarity Score = " ++ show similarityScore
