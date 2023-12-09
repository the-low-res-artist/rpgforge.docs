# Performance tests

This section covers the **Performance tests** results of **RPG Power Forge**.

These tests measure how efficient a feature is. With a given threshold (Doherty Threshold, more info [here](https://lawsofux.com/doherty-threshold/)), we can determine if the feature is fast enough ⚡ or too slow 🐌.

*In development, tests are added regularly*

## Context

Item|Value
---|---
version| 0.0.20
Unity version| 2021.3.25f1
Host OS| Windows 10 Family
Host spec| Intel Core i7 2.6GHz (12 cores) 32Go RAM
Date| May 31 2023   20: 17

## Summary

Total Tests|Fast ⚡|Slow 🐌
---|---|---
10|6|4

## Details

Test Name|Duration|Result
---|---|---
ImportAsset : CreateTilesCollection_256x256_Tile_16x16|822 ms|🐌
ImportAsset : CreateTilesCollection_768x768_Tile_48x48|957 ms|🐌
ImportAsset : ImportTileset_256x256_Tile_16x16|9 ms|⚡
ImportAsset : ImportTileset_768x768_Tile_48x48|9 ms|⚡
ImportAsset : Navigation|39 ms|⚡
ImportAsset : OpenWindow|332 ms|⚡
ImportAsset : SliceTileset_256x256_Tile_16x16|62 ms|⚡
ImportAsset : SliceTileset_768x768_Tile_48x48|56 ms|⚡
ImportAsset : ValidateTilesCollection_256x256_Tile_16x16|636 ms|🐌
ImportAsset : ValidateTilesCollection_768x768_Tile_48x48|1606 ms|🐌
