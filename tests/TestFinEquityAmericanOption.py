# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 10:04:57 2019

@author: Dominic
"""

import time

from financepy.finutils.FinTestCases import FinTestCases, globalTestCaseMode
from financepy.products.equity.FinEquityVanillaOption import FinEquityVanillaOption
from financepy.products.equity.FinEquityModelTypes import FinEquityModelBlackScholes
from financepy.products.FinOptionTypes import FinOptionTypes
from financepy.market.curves.FinFlatCurve import FinFlatCurve

from financepy.finutils.FinDate import FinDate
import sys
sys.path.append("..//..")

testCases = FinTestCases(__file__, globalTestCaseMode)


def testFinEquityAmericanOption():

    valueDate = FinDate(2016, 1, 1)
    expiryDate = FinDate(2017, 1, 1)
    stockPrice = 50.0
    interestRate = 0.06
    dividendYield = 0.04
    volatility = 0.40
    strikePrice = 50.0

    model = FinEquityModelBlackScholes(volatility)
    discountCurve = FinFlatCurve(valueDate, interestRate)

    numStepsList = [100, 200, 500, 1000, 2000]

    testCases.banner("================== EUROPEAN PUT =======================")

    putOption = FinEquityVanillaOption(
        expiryDate,
        strikePrice,
        FinOptionTypes.EUROPEAN_PUT)
    value = putOption.value(
        valueDate,
        stockPrice,
        discountCurve,
        dividendYield,
        model)
    delta = putOption.delta(
        valueDate,
        stockPrice,
        discountCurve,
        dividendYield,
        model)
    gamma = putOption.gamma(
        valueDate,
        stockPrice,
        discountCurve,
        dividendYield,
        model)
    theta = putOption.theta(
        valueDate,
        stockPrice,
        discountCurve,
        dividendYield,
        model)

    testCases.header("OPTION_TYPE", "VALUE", "DELTA", "GAMMA", "THETA")
    testCases.print("EUROPEAN_PUT_BS", value, delta, gamma, theta)

    option = FinEquityVanillaOption(
        expiryDate,
        strikePrice,
        FinOptionTypes.EUROPEAN_PUT)

    testCases.header(
        "OPTION_TYPE",
        "NUMSTEPS",
        "VALUE DELTA GAMMA THETA",
        "TIME")

    for numSteps in numStepsList:

        model = FinEquityModelBlackScholes(volatility, numSteps, True)
        start = time.time()
        results = option.value(
            valueDate,
            stockPrice,
            discountCurve,
            dividendYield,
            model)
        end = time.time()
        duration = end - start
        testCases.print("EUROPEAN_PUT_TREE", numSteps, results, duration)

    testCases.banner("================== AMERICAN PUT =======================")

    option = FinEquityVanillaOption(
        expiryDate,
        strikePrice,
        FinOptionTypes.AMERICAN_PUT)

    testCases.header(
        "OPTION_TYPE",
        "NUMSTEPS",
        "VALUE DELTA GAMMA THETA",
        "TIME")

    for numSteps in numStepsList:

        model = FinEquityModelBlackScholes(volatility, numSteps)
        start = time.time()
        results = option.value(
            valueDate,
            stockPrice,
            discountCurve,
            dividendYield,
            model)
        end = time.time()
        duration = end - start
        testCases.print("AMERICAN_PUT", numSteps, results, duration)

    testCases.banner(
        "================== EUROPEAN CALL =======================")

    callOption = FinEquityVanillaOption(
        expiryDate,
        strikePrice,
        FinOptionTypes.EUROPEAN_CALL)
    value = callOption.value(
        valueDate,
        stockPrice,
        discountCurve,
        dividendYield,
        model)
    delta = callOption.delta(
        valueDate,
        stockPrice,
        discountCurve,
        dividendYield,
        model)
    gamma = callOption.gamma(
        valueDate,
        stockPrice,
        discountCurve,
        dividendYield,
        model)
    theta = callOption.theta(
        valueDate,
        stockPrice,
        discountCurve,
        dividendYield,
        model)

    testCases.header("OPTION_TYPE", "VALUE", "DELTA", "GAMMA", "THETA")
    testCases.print("EUROPEAN_CALL_BS", value, delta, gamma, theta)

    option = FinEquityVanillaOption(
        expiryDate,
        strikePrice,
        FinOptionTypes.EUROPEAN_CALL)

    testCases.header(
        "OPTION_TYPE",
        "NUMSTEPS",
        "VALUE DELTA GAMMA THETA",
        "TIME")

    for numSteps in numStepsList:
        model = FinEquityModelBlackScholes(volatility, numSteps, True)
        start = time.time()
        results = option.value(
            valueDate,
            stockPrice,
            discountCurve,
            dividendYield,
            model)
        end = time.time()
        duration = end - start
        testCases.print("EUROPEAN_CALL_TREE", numSteps, results, duration)

    testCases.banner(
        "================== AMERICAN CALL =======================")
    testCases.header(
        "OPTION_TYPE",
        "NUMSTEPS",
        "VALUE DELTA GAMMA THETA",
        "TIME")

    option = FinEquityVanillaOption(
        expiryDate,
        strikePrice,
        FinOptionTypes.AMERICAN_CALL)

    for numSteps in numStepsList:
        model = FinEquityModelBlackScholes(volatility, numSteps)
        start = time.time()
        results = option.value(
            valueDate,
            stockPrice,
            discountCurve,
            dividendYield,
            model)
        end = time.time()
        duration = end - start
        testCases.print("AMERICAN_CALL", numSteps, results, duration)

#    FinTest.TestReport(filename)


testFinEquityAmericanOption()
testCases.compareTestCases()
