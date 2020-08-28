#ifndef SSC_H
#define SSC_H

#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui { class SSC; }
QT_END_NAMESPACE

class SSC : public QMainWindow
{
    Q_OBJECT

public:
    SSC(QWidget *parent = nullptr);
    ~SSC();

private slots:
    void Encryption();
    void strEdit(QString);
    void keyEdit(QString);
    QString getTextFromLine1();
    QString getTextFromLine2();
    void setTextToTB1(QString);
    void setTextToTB2(QString);
    int getShiftFromRB();

private:
    Ui::SSC *ui;
    QString alfabet = "abcdefghijklmnopqrstuvwxyz ";
};
#endif // SSC_H
