%global tl_name schule
%global tl_revision 77551

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.11.0
Release:	%{tl_revision}.1
Summary:	Support for teachers at German schools
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/schule
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/schule.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/schule.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The 'schule' bundle was built to provide packages and commands that
could be useful for documents in German schools. At the moment its main
focus lies on documents for informatics as a school subject. An
extension for physics is currently in progress. Extensions for other
subjects are welcome. For the time being, the whole package splits up
into individual packages for informatics (including syntax diagrams,
Nassi-Shneiderman diagrams, sequence diagrams, object diagrams, and
class diagrams) as well as classes for written exams (tests, quizzes,
teaching observations, information sheets, worksheets, and answer keys).

