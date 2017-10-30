km | minSpeed | MaxSpeed
--- | --- | --- |
0 - 200 | 15 | 34
200 - 400 | 15 | 32
400 - 600 | 15 | 30
600 - 1000 | 11.428 | 28

- Openning time <==> MaxSpeed
- Closing time <==> minSpeed

## Example

- Controle at 220km, 260km and 275km are governed by 34 and 32(openning), 15(closing).

km | Opening | Closing
--- | --- | ---|
220 | 200/34 + 20/32 = 5H53 +  0H38 = 6H31 | 220/15 = 14H40
260 | 200/34 + 60/32 = 5H53 + 1H53 = 7H46 | 260/15 = 17H20
275 | 200/34 + 75/32 = 5H53 + 2H20 = 8H13 | 275/15 = 18H20 

- Controle at 890km needs to be combined from multiple subcontrole; 890 = 200(first 200) + 200(2nd 200) + 200(3rd 200) + 290(4th range)
```
Opening: 200/34 + 200/32 + 200/30
```