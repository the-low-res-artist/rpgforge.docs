# Performance tests

This section covers the **Performance tests** results of **RPG Power Forge**.

These tests measure how efficient a feature is. With a given threshold (Doherty Threshold, more info [here](https://lawsofux.com/doherty-threshold/)), we can determine if the feature is fast enough ⚡ or too slow 🐌.

*In development, tests are added regularly*

## Context

Item|Value
---|---
RPG Power Forge version| 0.0.20
Unity version| 2021.3.25f1
Test Type| Performance
PC OS| Win32NT
PC OS version| 10.0.19045.0
PC host RAM| 31Go RAM
PC host CPU| Intel(R) Core(TM) i7-10750H CPU @ 2.60GHz (12 cores)
Date| May 28 2023
Time| 18:41

## Summary

Total Tests|Fast ⚡|Slow 🐌
---|---|---
10|6|4

## Details

Test Name|Duration|Result
---|---|---
ImportAsset : CreateTilesCollection_256x256_Tile_16x16|728 ms|🐌
ImportAsset : CreateTilesCollection_768x768_Tile_48x48|924 ms|🐌
ImportAsset : ImportTileset_256x256_Tile_16x16|2 ms|⚡
ImportAsset : ImportTileset_768x768_Tile_48x48|2 ms|⚡
ImportAsset : Navigation|9 ms|⚡
ImportAsset : OpenWindow|258 ms|⚡
ImportAsset : SliceTileset_256x256_Tile_16x16|27 ms|⚡
ImportAsset : SliceTileset_768x768_Tile_48x48|24 ms|⚡
ImportAsset : ValidateTilesCollection_256x256_Tile_16x16|657 ms|🐌
ImportAsset : ValidateTilesCollection_768x768_Tile_48x48|1543 ms|🐌