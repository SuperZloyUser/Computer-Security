#include "ssc.h"

#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    SSC w;
    w.show();
    return a.exec();
}
