/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2012/4/24 10:47:04                           */
/*==============================================================*/


drop table if exists CompilableCodeGenerationConfig;

drop table if exists CompileConfig;

drop table if exists Description;

drop table if exists InputOutputData;

drop table if exists KeywordCheckConfig;

drop table if exists OutputCheckConfig;

drop table if exists Permission;

drop table if exists Problem;

drop table if exists ProblemMeta;

drop table if exists RunConfig;

drop table if exists Submission;

drop table if exists TGroup;

drop table if exists User;

drop table if exists permissionGroup;

drop table if exists problemCCGC;

drop table if exists problemCompileConfig;

drop table if exists problemDescription;

drop table if exists problemIOData;

drop table if exists problemKeywordCheckConfig;

drop table if exists problemOutputCheckConfig;

drop table if exists problemRunConfig;

drop table if exists userGroup;

/*==============================================================*/
/* Table: CompilableCodeGenerationConfig                        */
/*==============================================================*/
create table CompilableCodeGenerationConfig
(
   id                   int not null auto_increment,
   problem_meta_id      int,
   code_type_id         int,
   generation_method    varchar(254),
   requirment           int,
   primary key (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*==============================================================*/
/* Table: CompileConfig                                         */
/*==============================================================*/
create table CompileConfig
(
   id                   int not null auto_increment,
   problem_meta_id      int,
   code_type            int,
   config               varchar(254),
   primary key (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*==============================================================*/
/* Table: Description                                           */
/*==============================================================*/
create table Description
(
   id                   int not null auto_increment,
   title                varchar(254),
   content              varchar(254),
   input                varchar(254),
   output               varchar(254),
   sample_input         varchar(254),
   sample_output        varchar(254),
   hint                 varchar(254),
   source               varchar(254),
   problem_meta_id      int,
   primary key (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*==============================================================*/
/* Table: InputOutputData                                       */
/*==============================================================*/
create table InputOutputData
(
   id                   int not null auto_increment,
   name                 varchar(254),
   problem_meta_id      int,
   primary key (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*==============================================================*/
/* Table: KeywordCheckConfig                                    */
/*==============================================================*/
create table KeywordCheckConfig
(
   id                   int not null auto_increment,
   problem_meta_id      int,
   code_type            int,
   word                 varchar(254),
   primary key (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*==============================================================*/
/* Table: OutputCheckConfig                                     */
/*==============================================================*/
create table OutputCheckConfig
(
   id                   int not null auto_increment,
   problem_meta_id      int,
   check_method         varchar(254),
   primary key (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*==============================================================*/
/* Table: Permission                                            */
/*==============================================================*/
create table Permission
(
   id                   int not null auto_increment,
   name                 int,
   primary key (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*==============================================================*/
/* Table: Problem                                               */
/*==============================================================*/
create table Problem
(
   id                   int not null auto_increment,
   problem_meta_id      int,
   judge_flow           varchar(254),
   primary key (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*==============================================================*/
/* Table: ProblemMeta                                           */
/*==============================================================*/
create table ProblemMeta
(
   id                   int not null auto_increment,
   title                varchar(254),
   judge_flow           varchar(254),
   primary key (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*==============================================================*/
/* Table: RunConfig                                             */
/*==============================================================*/
create table RunConfig
(
   id                   int not null auto_increment,
   problem_meta_id      int,
   code_type            int,
   time                 int,
   memory               int,
   primary key (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*==============================================================*/
/* Table: Submission                                            */
/*==============================================================*/
create table Submission
(
   id                   int not null auto_increment,
   problem_id           int,
   user_id              int,
   sub_time             datetime,
   status               int,
   used_time            int,
   used_memory          int,
   primary key (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*==============================================================*/
/* Table: TGroup                                                */
/*==============================================================*/
create table TGroup
(
   id                   int not null auto_increment,
   name                 int,
   primary key (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*==============================================================*/
/* Table: User                                                  */
/*==============================================================*/
create table User
(
   id                   int not null auto_increment,
   username             varchar(254),
   password             varchar(254),
   nickname             varchar(254),
   email                varchar(254),
   submit               int,
   accept               int,
   reg_time             datetime,
   primary key (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*==============================================================*/
/* Table: permissionGroup                                       */
/*==============================================================*/
create table permissionGroup
(
   permission_id        int not null,
   group_id             int not null,
   primary key (permission_id, group_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*==============================================================*/
/* Table: problemCCGC                                           */
/*==============================================================*/
create table problemCCGC
(
   problem_id           int not null,
   ccgc_id              int not null,
   primary key (problem_id, ccgc_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*==============================================================*/
/* Table: problemCompileConfig                                  */
/*==============================================================*/
create table problemCompileConfig
(
   problem_id           int not null,
   compileconfig_id     int not null,
   primary key (problem_id, compileconfig_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*==============================================================*/
/* Table: problemDescription                                    */
/*==============================================================*/
create table problemDescription
(
   description_id       int not null,
   problem_id           int not null,
   primary key (description_id, problem_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*==============================================================*/
/* Table: problemIOData                                         */
/*==============================================================*/
create table problemIOData
(
   problem_id           int not null,
   io_id                int not null,
   primary key (problem_id, io_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*==============================================================*/
/* Table: problemKeywordCheckConfig                             */
/*==============================================================*/
create table problemKeywordCheckConfig
(
   keyconfig_id         int not null,
   problem_id           int not null,
   primary key (keyconfig_id, problem_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*==============================================================*/
/* Table: problemOutputCheckConfig                              */
/*==============================================================*/
create table problemOutputCheckConfig
(
   problem_id           int not null,
   outputcheck_id       int not null,
   primary key (problem_id, outputcheck_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*==============================================================*/
/* Table: problemRunConfig                                      */
/*==============================================================*/
create table problemRunConfig
(
   problem_id           int not null,
   runconfig_id         int not null,
   primary key (problem_id, runconfig_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*==============================================================*/
/* Table: userGroup                                             */
/*==============================================================*/
create table userGroup
(
   user_id              int not null,
   group_id             int not null,
   primary key (user_id, group_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

alter table CompilableCodeGenerationConfig add constraint FK_association7 foreign key (problem_meta_id)
      references ProblemMeta (id) on delete restrict on update restrict;

alter table CompileConfig add constraint FK_association8 foreign key (problem_meta_id)
      references ProblemMeta (id) on delete restrict on update restrict;

alter table Description add constraint FK_Relationship_29 foreign key (problem_meta_id)
      references ProblemMeta (id) on delete restrict on update restrict;

alter table InputOutputData add constraint FK_association10 foreign key (problem_meta_id)
      references ProblemMeta (id) on delete restrict on update restrict;

alter table KeywordCheckConfig add constraint FK_association6 foreign key (problem_meta_id)
      references ProblemMeta (id) on delete restrict on update restrict;

alter table OutputCheckConfig add constraint FK_association11 foreign key (problem_meta_id)
      references ProblemMeta (id) on delete restrict on update restrict;

alter table Problem add constraint FK_association18 foreign key (problem_meta_id)
      references ProblemMeta (id) on delete restrict on update restrict;

alter table RunConfig add constraint FK_association9 foreign key (problem_meta_id)
      references ProblemMeta (id) on delete restrict on update restrict;

alter table Submission add constraint FK_association20 foreign key (user_id)
      references User (id) on delete restrict on update restrict;

alter table Submission add constraint FK_association5 foreign key (problem_id)
      references Problem (id) on delete restrict on update restrict;

alter table permissionGroup add constraint FK_permissionGroup foreign key (permission_id)
      references Permission (id) on delete restrict on update restrict;

alter table permissionGroup add constraint FK_permissionGroup1 foreign key (group_id)
      references TGroup (id) on delete restrict on update restrict;

alter table problemCCGC add constraint FK_problemCCGC foreign key (ccgc_id)
      references CompilableCodeGenerationConfig (id) on delete restrict on update restrict;

alter table problemCCGC add constraint FK_problemCCGC1 foreign key (problem_id)
      references Problem (id) on delete restrict on update restrict;

alter table problemCompileConfig add constraint FK_problemCompileConfig foreign key (compileconfig_id)
      references CompileConfig (id) on delete restrict on update restrict;

alter table problemCompileConfig add constraint FK_problemCompileConfig1 foreign key (problem_id)
      references Problem (id) on delete restrict on update restrict;

alter table problemDescription add constraint FK_problemDescription foreign key (description_id)
      references Description (id) on delete restrict on update restrict;

alter table problemDescription add constraint FK_problemDescription1 foreign key (problem_id)
      references Problem (id) on delete restrict on update restrict;

alter table problemIOData add constraint FK_problemIOData foreign key (io_id)
      references InputOutputData (id) on delete restrict on update restrict;

alter table problemIOData add constraint FK_problemIOData1 foreign key (problem_id)
      references Problem (id) on delete restrict on update restrict;

alter table problemKeywordCheckConfig add constraint FK_problemKeywordCheckConfig foreign key (keyconfig_id)
      references KeywordCheckConfig (id) on delete restrict on update restrict;

alter table problemKeywordCheckConfig add constraint FK_problemKeywordCheckConfig1 foreign key (problem_id)
      references Problem (id) on delete restrict on update restrict;

alter table problemOutputCheckConfig add constraint FK_problemOutputCheckConfig foreign key (outputcheck_id)
      references OutputCheckConfig (id) on delete restrict on update restrict;

alter table problemOutputCheckConfig add constraint FK_problemOutputCheckConfig1 foreign key (problem_id)
      references Problem (id) on delete restrict on update restrict;

alter table problemRunConfig add constraint FK_problemRunConfig foreign key (problem_id)
      references Problem (id) on delete restrict on update restrict;

alter table problemRunConfig add constraint FK_problemRunConfig1 foreign key (runconfig_id)
      references RunConfig (id) on delete restrict on update restrict;

alter table userGroup add constraint FK_userGroup foreign key (group_id)
      references TGroup (id) on delete restrict on update restrict;

alter table userGroup add constraint FK_userGroup1 foreign key (user_id)
      references User (id) on delete restrict on update restrict;

