{-# OPTIONS -fno-warn-tabs #-}

import Data.Array ((!))
import qualified Data.Array as Array 

main :: IO ()
main = do
	contents <- getContents
	putStrLn $ handle $ filter (/= "") $ lines contents

handle :: [String] -> String
handle (sourceString : stringK : strings) = if resultDistance > k then "-1" else show resultIndex ++ "\n" ++ show resultDistance
	where
		k = read stringK :: Int
		indexed = zip [1..] strings
		f (i, s) = IndexedInt (i, distance sourceString s)
		(resultIndex, resultDistance) = get $ minimum $ map f indexed


newtype IndexedInt = IndexedInt {get :: (Int, Int)} deriving Eq

instance Ord IndexedInt where
	(IndexedInt (_, x)) <= (IndexedInt (_, y)) = x <= y


distance :: String -> String -> Int
distance a b = d m n
  where (m, n) = (length a, length b)
        a'     = Array.listArray (1, m) a
        b'     = Array.listArray (1, n) b

        d i 0 = i
        d 0 j = j
        d i j
          | a' ! i ==  b' ! j = ds ! (i - 1, j - 1)
          | otherwise = minimum [ ds ! (i - 1, j)     + 1
                                , ds ! (i, j - 1)     + 1
                                , ds ! (i - 1, j - 1) + 1
                                ]

        ds = Array.listArray bounds
               [d i j | (i, j) <- Array.range bounds]
        bounds = ((0, 0), (m, n))
