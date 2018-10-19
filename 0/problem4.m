% Problem 4
% largest palindrome that is the product of two three digit numbers

% guessing that the two facts will both be larger than 900, create
% a three dimensional matrix and compare digits.
% by inspection find largest palindrome of these

products = zeros(100, 100);

for i = 1:100
    for j = 1:100
        products(i,j) = (899+i)*(899+j);
    end
end

digits = zeros(100, 100, 6);
for i = 1:100
    for j = 1:100
        for k = 1:6
            x = num2str(products(i,j));
            digits(i, j, k) = str2num(x(k));
        end
    end
end

for i = 1:100
    for j = 1:100
        if (digits(i,j,1) == digits(i,j,6)) && (digits(i,j,2)==digits(i,j,5)) && (digits(i,j,3)== digits(i,j,4))
            fprintf('%d \n', products(i,j));
        end
    end
end
