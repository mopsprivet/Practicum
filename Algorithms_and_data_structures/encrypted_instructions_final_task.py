# id посылки: 142640270 

import string 


def decode_instructions(enc_instructions: str) -> str:
    """Функция для расшифровки инструкций марсохода."""
    stack: list[tuple[str, int]] = []
    current_instruction: str = ""
    current_number: str = ""
    
    for item in enc_instructions:
        if item in string.digits:
            current_number += item
        elif item == '[': 
            multiplier: int
            if current_number:
                multiplier = int(current_number)
            else:
                multiplier = 1
            stack.append((current_instruction, multiplier))
            current_instruction = ""
            current_number = ""
        elif item == ']':
            prev_string, mult_times = stack.pop()
            current_instruction = prev_string + current_instruction * mult_times
        else:
            current_instruction += item
    
    return current_instruction


if __name__ == '__main__':
    input_command: str = input().strip()
    print(decode_instructions(input_command))