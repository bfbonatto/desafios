{-# OPTIONS -fno-warn-tabs #-}


dpLCS :: String -> String -> Int
dpLCS _ [] = 0
dpLCS a b =
  let nextRow ac prevRow =
        let diagonals = 0:prevRow
            lefts = 0:thisRow
            ups = prevRow
            maxes = zipWith max lefts ups
            thisRow = zipWith3 (\diag maxLeftUp bc ->
                                   if bc == ac then 1 + diag else maxLeftUp)
                                   diagonals maxes b
        in thisRow

      firstRow = map (const 0) b
      dpTable = firstRow:zipWith nextRow a dpTable

  in last (last dpTable)

main :: IO ()
main = undefined
