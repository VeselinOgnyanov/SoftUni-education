british_pounds_to_be_converted = int(input())


def convertor_gbr_to_usd(british_pounds):
    gbr_to_usd = 1.31
    result = british_pounds * gbr_to_usd
    return result


converted_value = convertor_gbr_to_usd(british_pounds_to_be_converted)
print(f"{converted_value:.3f}")
