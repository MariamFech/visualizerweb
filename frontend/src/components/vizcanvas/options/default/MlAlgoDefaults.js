export function kMeans () {
  return {
    mlAlgoName: 'K-Means',
    mlAlgoOptions: {
      Cluster: 2,
      Iterations: 300,
      'Centroid Seeds': 4
    }
  }
}
export function hierarchical () {
  return {
    mlAlgoName: 'Hierarchical',
    mlAlgoOptions: {
      Cluster: 2,
      Linkage: 'ward'
    }
  }
}
export function decisionTree () {
  return {
    mlAlgoName: 'Decision Tree',
    mlAlgoOptions: {
      Depth: 2
    }
  }
}
export function nearestNeighbors () {
  return {
    mlAlgoName: 'Nearest Neighbors',
    mlAlgoOptions: {
      Neighbors: 2
    }
  }
}
export function suvm () {
  return {
    mlAlgoName: 'SVM',
    mlAlgoOptions: {
      C: 1,
      Kernel: 'rbf'
    }
  }
}
export function regressionTree () {
  return {
    mlAlgoName: 'Regression Tree',
    mlAlgoOptions: {
      Depth: 1,
      Samples: 1
    }
  }
}
export function linearRegression () {
  return {
    mlAlgoName: 'Linear Regression',
    mlAlgoOptions: {
      Degree: 1
    }
  }
}
