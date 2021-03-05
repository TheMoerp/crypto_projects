def ea(num1, num2):
    r = [num1, num2];
    i = 1;
    while (True): 
        i += 1;
        r.append(r[i - 2] % r[i - 1]);
        if (r[i] == 0):
            break
    return r[i - 1];
