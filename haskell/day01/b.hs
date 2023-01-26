import Data.List

splitOn :: Eq a => a -> [a] -> [[a]]
splitOn x y = splitOnHelper x y [] [] where
    splitOnHelper :: Eq a => a -> [a] -> [a] -> [[a]] -> [[a]]
    splitOnHelper x [] acc res = res ++ [acc]
    splitOnHelper x (y : ys) acc res | x == y = splitOnHelper x ys [] (res ++ [acc])
                                     | otherwise = splitOnHelper x ys (acc ++ [y]) res

main = do
    content <- Prelude.readFile "input.txt"
    let values :: [[Integer]] = map (map read) $ splitOn [] $ lines content
    let caloriesByElf = map sum values
    print(sum $ take 3 $ reverse $ sort caloriesByElf)
