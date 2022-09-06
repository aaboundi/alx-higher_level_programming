#!/usr/bin/node
const s = Math.floor(Number(process.argv[2]));
if (isNaN(s)) {
	console.log('Missing size');
}
else {
	for (let i = 0; i < s; i++) {
		let square = '';
		for (let j = 0; j < s; j++) square += 'X';
		console.log(square);
	}
}
