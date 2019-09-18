#!/usr/bin/node
const l = process.argv.length;
if (l < 4) {
  console.log(0);
} else {
  const args = process.argv.slice(2);
  args.sort(function (a, b) { return b - a; });
  console.log(args[1]);
}
