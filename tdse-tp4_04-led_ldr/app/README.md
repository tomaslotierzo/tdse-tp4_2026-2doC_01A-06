# tdse-tp4_04-led_ldr

## Description:
 task/task interaction. 
 LED (output) Pulse Width Modulation -> LDR (input) reading -> show values on console.
 App - retarget_printf_to_Console
 Project for STM32 Project (STM32CubeIDE Version: 1.7.0)

  SystemCoreClock     => 64MHz (15.625nS)
  SysTick Rate Hertz  => 1000 ticks per second (1mS)

  app.c (app.h)
   Endless loops, which execute tasks with fixed computing time. This 
   sequential execution is only deviated from when an interrupt event occurs.

  task_adc.c (task_adc.h) 
   Initializes ADC for single conversion. The loop busy waits for a new conversion and raises a flag.

  task_pwm.c (task_pwm.h)
   Initializes PWM output on PA6. The loop waits for ADC end of conversion flag, then changes the duty cycle.

  logger.h (logger.c)
   Utilities for Retarget "printf" to Console

  dwt.h
   Utilities for Measure "clock cycle" and "execution time" of code
  
  Special connection requirements:
   There are no special connection requirements for this example.

Build procedures:
Visit the Getting started with STM32: STM32 step-by-step at 
"https://wiki.st.com/stm32mcu/wiki/STM32StepByStep:Getting_started_with_STM32_:_STM32_step_by_step"
to get started building STM32 Projects.

