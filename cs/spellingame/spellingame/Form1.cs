﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace spellingame
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void buttonSubmit_Click(object sender, EventArgs e)
        {

        }
        private void StartRound()
        {
            textBoxWord.Text = "Test";
        }

        private void buttonBegin_Click(object sender, EventArgs e)
        {
            buttonBegin.Visible = false;
            StartRound();
        }

        private void timer1_Tick(object sender, EventArgs e)
        {

        }
    }
}
