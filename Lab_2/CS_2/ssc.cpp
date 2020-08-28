#include "ssc.h"
#include "ui_ssc.h"
#include "func.cpp"


SSC::SSC(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::SSC)
{
    ui->setupUi(this);

    connect(ui->pushButton, SIGNAL(clicked()), this, SLOT(GenPQ()));
    connect(ui->lineEdit, SIGNAL(textEdited(QString)), this, SLOT(strEdit(QString)));
    connect(ui->lineEdit_2, SIGNAL(textEdited(QString)), this, SLOT(keyEdit(QString)));

}


void SSC::GenPQ()
{

}


void SSC::strEdit(QString change)
{

    QString newStr;

    for (int i = 0; i < change.length(); i++)
        if (alfabet.indexOf(change[i], 0, Qt::CaseInsensitive) != -1) newStr = newStr + change[i];

    ui->lineEdit->setText(newStr);

}


void SSC::keyEdit(QString change)
{

    QString newStr;

    for (int i = 0; i < change.length(); i++)
        if (alfabet.indexOf(change[i], 0, Qt::CaseInsensitive) != -1 &&
                alfabet.indexOf(change[i], 0, Qt::CaseInsensitive) != 26) newStr = newStr + change[i];

    ui->lineEdit_2->setText(newStr);

}


QString SSC::getTextFromLine1(){
    return ui->lineEdit->text();
}


QString SSC::getTextFromLine2(){
    return ui->lineEdit_2->text();
}


void SSC::setTextToTB1(QString temp){
    return ui->textBrowser->setText(temp);
}


void SSC::setTextToTB2(QString temp){
    return ui->textBrowser_2->setText(temp);
}


SSC::~SSC()
{
    delete ui;
}
