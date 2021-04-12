/**
 * Colormap 'rainbow_discrete' from tol_colors.py by Paul Tol implemented in Javascript.
 *
 * Original:
 * Definition of colour schemes for lines and maps that also work for colour-blind
 * people. See https://personal.sron.nl/~pault/ for background information and
 * best usage of the schemes.
 * Copyright (c) 2019, Paul Tol
 * All rights reserved.
 *
 * License:  Standard 3-clause BSD
 */

const rainbowDiscrete = ['#E8ECFB', '#D9CCE3', '#D1BBD7', '#CAACCB',
  '#BA8DB4', '#AE76A3', '#AA6F9E', '#994F88', '#882E72',
  '#1965B0', '#437DBF', '#5289C7', '#6195CF', '#7BAFDE',
  '#4EB265', '#90C987', '#CAE0AB', '#F7F056', '#F7CB45',
  '#F6C141', '#F4A736', '#F1932D', '#EE8026', '#E8601C',

  '#E65518', '#DC050C', '#A5170E', '#72190E', '#42150A']

const indexes = [
  [9],
  [9, 25],
  [9, 17, 25],
  [9, 14, 17, 25],
  [9, 13, 14, 17, 25],
  [9, 13, 14, 16, 17, 25],
  [8, 9, 13, 14, 16, 17, 25],
  [8, 9, 13, 14, 16, 17, 22, 25],
  [8, 9, 13, 14, 16, 17, 22, 25, 27],
  [8, 9, 13, 14, 16, 17, 20, 23, 25, 27],
  [8, 9, 11, 13, 14, 16, 17, 20, 23, 25, 27],
  [2, 5, 8, 9, 11, 13, 14, 16, 17, 20, 23, 25],
  [2, 5, 8, 9, 11, 13, 14, 15, 16, 17, 20, 23, 25],
  [2, 5, 8, 9, 11, 13, 14, 15, 16, 17, 19, 21, 23, 25],
  [2, 5, 8, 9, 11, 13, 14, 15, 16, 17, 19, 21, 23, 25, 27],
  [2, 4, 6, 8, 9, 11, 13, 14, 15, 16, 17, 19, 21, 23, 25, 27],
  [2, 4, 6, 7, 8, 9, 11, 13, 14, 15, 16, 17, 19, 21, 23, 25, 27],
  [2, 4, 6, 7, 8, 9, 11, 13, 14, 15, 16, 17, 19, 21, 23, 25, 26, 27],
  [1, 3, 4, 6, 7, 8, 9, 11, 13, 14, 15, 16, 17, 19, 21, 23, 25, 26, 27],
  [1, 3, 4, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 19, 21, 23, 25, 26, 27],
  [1, 3, 4, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 20, 22, 24, 25, 26, 27],
  [1, 3, 4, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 20, 22, 24, 25, 26, 27, 28],
  [0, 1, 3, 4, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 20, 22, 24, 25, 26, 27, 28]
]

export function getColors (int) {
  const colors = []
  indexes[int - 1].forEach(el => {
    colors.push(rainbowDiscrete[el])
  })
  return colors
}
