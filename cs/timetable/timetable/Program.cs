using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace timetable
{
    internal class Program
    {
        /// <summary>
        /// Display all times tables from one to twelve.
        /// </summary>
        /// <param name="args"></param>
        static void Main(string[] args)
        {
            // loop that counting from one to twelve
            for (int i = 1; i < 13; i++)
            {
                // create a second loop for multiplier, one to twelve
                for (int j = 1; j < 13; j++)
                {
                    Console.WriteLine($"{i} x {j} = {i * j}");
                }
            }
        }
    }
}
