#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  if (list.length > 0) {
    for (const item of list) {
      if (item === searchElement) { count++; }
    }
  }
  return count;
};
