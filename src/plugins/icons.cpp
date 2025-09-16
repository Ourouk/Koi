#include "icons.h"

#include <QProcess>

void Icons::setTheme(QString iconTheme) {

  // locate plasma-changeicons program
  QProcess process;
  QString locateProgram = "whereis";
  QStringList programToLocate = {"plasma-changeicons"};

  process.start(locateProgram, programToLocate);
  process.waitForFinished();

  QString program(process.readAllStandardOutput());
  program.replace("plasma-changeicons: ", "");
  program.replace("\n", "");

  // apply the icon theme
  QStringList arguments{iconTheme};
  QProcess::startDetached(program, arguments);
}

QStringList Icons::getThemes() {
  QDir iconsOldLocalDir(QDir::homePath() + "/.icons");
  QDir iconsLocalDir(QDir::homePath() + "/.local/share/icons");
  QDir iconsSystemDir("/usr/share/icons");
  QDir iconsNixDir("/run/current-system/profile/share/icons");
  QStringList iconThemes;
  if (iconsOldLocalDir.exists()) {
    iconThemes = iconThemes +
                 iconsOldLocalDir.entryList(QDir::Dirs | QDir::NoDotAndDotDot);
  }
  if (iconsLocalDir.exists()) {
    iconThemes =
        iconThemes + iconsLocalDir.entryList(QDir::Dirs | QDir::NoDotAndDotDot);
  }
  if (iconsSystemDir.exists()) {
    iconThemes = iconThemes +
                 iconsSystemDir.entryList(QDir::Dirs | QDir::NoDotAndDotDot);
  }
  if (iconsNixDir.exists()) {
    iconThemes =
        iconThemes + iconsNixDir.entryList(QDir::Dirs | QDir::NoDotAndDotDot);
  }
  iconThemes.removeDuplicates();
  iconThemes.sort();
  return iconThemes;
}
