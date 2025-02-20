qRolls = 0
dRolls = 0
nRolls = 0
pRolls = 0

qNum = int(input("How many quarters? "))
dNum = int(input("   How many dimes? "))
nNum = int(input(" How many nickels? "))
pNum = int(input(" How many pennies? "))
print("")

qMoney = float(qNum * .25)
dMoney = float(dNum * .10)
nMoney = float(nNum * .05)
pMoney = float(pNum * .01)

totalCoins = qNum + dNum + nNum + pNum
totalMoney = qMoney + dMoney + nMoney + pMoney

print("Quarters:".rjust(20), "%i".rjust(20) % qNum, " x 0.25¢ = $".rjust(20), qMoney.rjust(20))
print("Dimes:".rjust(20), "%i".rjust(20) % dNum, " x 0.10¢ = $".rjust(20), dNum.rjust(20))
print("Nickels:".rjust(20), nNum, " x 0.05¢ = $".rjust(20), nNum.rjust(20))
print("Pennies:".rjust(20), pNum.rjust(20), " x 0.25¢ = $".rjust(20), pNum.rjust(20))

print("\nYour %i coins are worth $%.2f" % (totalCoins, totalMoney))

if input("would you like to roll the coins?") == "y":
  while qNum >= 40:
    qRolls = qRolls + 1
    qNum = qNum - 40 
  while dNum >= 50:
    dRolls = dRolls + 1
    dNum = dNum - 50
  while nNum >= 40:
    nRolls = dRolls + 1
    nNum = nNum - 40
  while pNum >= 50:
    pRolls = pRolls + 1
    pNum = pNum - 50

print("\nyou have %i rolls of quarters and %i quarters left over" % (qRolls, qNum))
print("you have %i rolls of dimes and %i dimes left over" % (dRolls, dNum))
print("you have %i rolls of nickles and %i nickles left over" % (nRolls, nNum))
print("you have %i rolls of pennies and %i pennies left over" % (pRolls, pNum))